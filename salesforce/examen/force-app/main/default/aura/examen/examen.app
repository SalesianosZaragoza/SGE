<aura:application>
   <c:OwnerForm></c:OwnerForm>
   <c:OwnerList></c:OwnerList>
   <c:PetForm></c:PetForm>
   <c:PetList></c:PetList>
   <c:LinkedList></c:LinkedList>
    <aura:registerEvent name="insertOwner" type="c:insertOwner"/>
    <aura:registerEvent name="insertPet" type="c:insertPet"/>
    <aura:registerEvent name="linkPet" type="c:linkOwner"/>
    <aura:registerEvent name="linkOwner" type="c:linkPet"/>
   <c:linkOwnerPet></c:linkOwnerPet>
   <c:OwnerPetList></c:OwnerPetList>
    <aura:registerEvent name="doLink" type="c:doLink"/>
</aura:application>	
