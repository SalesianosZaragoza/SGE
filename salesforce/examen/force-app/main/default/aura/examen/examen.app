<aura:application>
   <c:OwnerForm></c:OwnerForm>
   <c:OwnerList></c:OwnerList>
   <c:PetForm></c:PetForm>
   <c:PetList></c:PetList>
   <c:linkOwnerPet></c:linkOwnerPet>
   <c:OwnerPetList></c:OwnerPetList>
    <aura:registerEvent name="insertOwner" type="c:insertOwner"/>
    <aura:registerEvent name="insertPet" type="c:insertPet"/>
    <aura:registerEvent name="doLink" type="c:doLink"/>
</aura:application>	
