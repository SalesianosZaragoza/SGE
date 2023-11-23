from datetime import timedelta
from odoo import models, fields, api, exceptions

class Bodega(models.Model):
    _name = 'vinoteca.bodega'

    name = fields.Char(string="Bodega", required=True)
    description = fields.Text(string="Información adicional")

    productos_ids = fields.One2many('vinoteca.producto', 'bodega_id', string="Productos")


class Producto(models.Model):
    _name = 'vinoteca.producto'

    name = fields.Char(string="Nombre del producto", required=True)
    code = fields.Char(string="Codigo", required=True)
    price = fields.Float(string="Precio", digits=(4, 2), required=True)
    typeContainer = fields.Char(string="Tipo de envase", required=True)

    bodega_id = fields.Many2one('vinoteca.bodega', ondelete='cascade', string="Bodega")

    compras_ids = fields.Many2many('vinoteca.compra', string="Compras")

    @api.multi
    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [('code', '=like', u"Copia de {}%".format(self.code))])
        if not copied_count:
            new_code = u"Copia de {}".format(self.code)
        else:
            new_code = u"Copia de {} ({})".format(self.code, copied_count)

        default['code'] = new_code
        return super(Producto, self).copy(default)

    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != code)',
         "El nombre y el codigo no pueden ser iguales"),

        ('code_unique',
         'UNIQUE(code)',
         "El codigo debe ser unico"),
    ]

    @api.constrains('price')
    def _check_price_not_negative(self):
        for r in self:
            if r.price < 0.00:
                raise exceptions.ValidationError("El precio no puede ser negativo")


class Zumo(models.Model):
    _name = 'vinoteca.zumo'
    _inherit = 'vinoteca.producto'

    sugar = fields.Float(string="Cantidad de azucar", digits=(2, 2), help="En gr por cada 100ml", required=True)
    pulpa = fields.Boolean(string="Pulpa", default=True, required=True)

    percentage_sugar = fields.Float(string="Porcentaje de azucar", help="Siendo 25 gramos el consumo máximo recomendado por la OMS", compute='_percentage_sugar')

    @api.depends('sugar')
    def _percentage_sugar(self):
        for r in self:
            if not r.sugar:
                r.percentage_sugar = 0.00
            else:
                r.percentage_sugar = 100.00 * r.sugar / 25.00

    @api.onchange('sugar')
    def _verify_valid_sugar(self):
        if self.sugar < 0.00:
            return {
                'warning': {
                    'title': "Valor incorrecto",
                    'message': "La cantidad de azúcar no puede ser negativa",
                },
            }


class Cliente(models.Model):
    _name = 'vinoteca.cliente'

    name = fields.Char(string="Nombre", required=True)

    compras_ids = fields.One2many('vinoteca.compra', 'cliente_id', string="Compras")


class Compra(models.Model):
    _name = 'vinoteca.compra'

    code = fields.Char(string="Codigo", required=True)
    date = fields.Date(string="Fecha de compra", default=fields.Date.today, required=True)

    cliente_id = fields.Many2one('vinoteca.cliente', ondelete='cascade', string="Cliente")

    productos_ids = fields.Many2many('vinoteca.producto', string="Productos")

    color = fields.Integer()