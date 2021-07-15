
function validate(form)
{
if(form.FullName.value=="")
  {
    alert("Name cannot be blanked");
	return;
   }
 if(form.ContactNo.value=="")
  {
    alert("Contact Number cannot be blanked");
	return;
  } 
  if(form.EmailId.value="")
   {
     alert("Email Id cannot be blanked");
	}
  if(form.Age.value=="" && form.age.value<18)
  {
    alert("enter age and age should be greater than 18");
	return;
   }
   if(form.gender.value=="")
  {
    alert("Gender cannot be blanked");
	return;
   }
   if(form.Address.value=="")
  {
    alert("Address cannot be blanked");
	return;
   }
  
  alert("Thankyou for registration. We will contact you");
 }
