function validation(form)
{
if(form.Name.value=="")
  {
    alert("Name cannot be blanked");
	return;
   }
 if(form.doctorName.value=="")
  {
    alert("Doctor Name cannot be blanked");
	return;
  } 
  if(form.EmailId.value="")
   {
     alert("Email Id cannot be blanked");
	}
  if(form.MobileNo.value=="")
  {
    alert("Mobile Number cannot be blanked");
	return;
   }
   if(form.ContactName.value=="")
  {
    alert("Contact Name cannot be blanked");
	return;
   }
   if(form.Address.value=="")
  {
    alert("Address cannot be blanked");
	return;
   }
  
  alert("We got your request. We will contact you. Thankyou");
 }