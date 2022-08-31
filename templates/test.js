function check(form) {
    if(form.userid.value=="doosan") {
       if(form.userpassword.value=="1234") {
             window.open('target.html')
       } else {
           alert('비밀번호가 유효하지 않습니다.');
       }
} else {
    alert('존재하지 않는 아이디 입니다.'
    )}
}
