function singleInsert() {
    var infos = {};
    infos['email'] = document.getElementsByName('email')[0].value
    infos['username'] = document.getElementsByName('username')[0].value
    infos['password'] = document.getElementsByName('password')[0].value
    infos['database'] = document.getElementsByName('database')[0].value
    $.ajax({
    url: '/singleInsert',
    type: 'POST',
    data: JSON.stringify(infos),
    contentType: 'application/json; charset=utf-8',
    dataType: 'json',
    async: false,
    success: function(msg) {
        alert(msg['message']);
    }
    });
}


function searchbyEmail() {
var infos = {};
$('#leaksresultEmail').html("")
infos['search'] = document.getElementsByName('email-search')[0].value
infos['searchby'] = 'email'
$.ajax({
    url: '/search',
    type: 'POST',
    data: JSON.stringify(infos),
    contentType: 'application/json; charset=utf-8',
    dataType: 'json',
    async: false,
    success: function(data) {
        data.forEach(function(leak, index) {
          $('#leaksresultEmail').append('<tr><td>'+escape(leak.email)+'</td><td>'+escape(leak.username)+'</td><td>'+escape(leak.password)+'</td><td>'+escape(leak.database)+'</td><td><a href="/delete/'+escape(leak.id)+'">delete</a></td></tr>')
        });
    }
});
}

function searchbyPassword() {
var infos = {};
$('#leaksresultPassword').html("")
infos['search'] = document.getElementsByName('password-search')[0].value
infos['searchby'] = 'password'
$.ajax({
    url: '/search',
    type: 'POST',
    data: JSON.stringify(infos),
    contentType: 'application/json; charset=utf-8',
    dataType: 'json',
    async: false,
    success: function(data) {
        data.forEach(function(leak, index) {
          $('#leaksresultPassword').append('<tr><td>'+escape(leak.email)+'</td><td>'+escape(leak.username)+'</td><td>'+escape(leak.password)+'</td><td>'+escape(leak.database)+'</td><td><a href="/delete/'+escape(leak.id)+'">delete</a></td></tr>')
        });
    }
});
}
