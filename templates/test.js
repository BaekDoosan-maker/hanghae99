function check(form) {
    if(form.userid.value=="doosan") {
       if(form.userpassword.value=="1234") {
             window.open('target.html')
       } else {
           alert('Error Password');
       }
} else {
    alert('Error UserID'
    )}
}
