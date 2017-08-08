$(function(){
    
function msg(m){
    $("#resultat").html(m);
}

function getAuth(){ 
    $.ajax({
            method: "POST",
                url: "fw_authentification.py",
                data: { 
                    pwd: SHA256($("#pwd").val()),
                    usr: $("#usr").val(),
                    redirige: $("#redirige").val(),
                }
        })
        .done(
            function(reponse) {
                reponse = JSON.parse(reponse);
                msg(reponse.commentaire);
                if(reponse.idSession != ""){
                    setCookie("idSession", $.trim(reponse.idSession), 1);
                    setCookie("usr", $("#usr").val(), 1);
                }
                
                if(reponse.redirige != undefined && reponse.redirige != ""){
                    document.location = reponse.redirige;
                } 
        });
        
    return false;
}

function unLog(){
    $.ajax({
            method: "POST",
                url: "fw_finSession.py",
        })
        .done(
            function(reponse) {
                reponse = JSON.parse(reponse);
                msg(reponse.commentaire);
                
                if(getCookie("idSession")){
                    deleteCookie("idSession");
                }
                if(getCookie("usr")){
                    deleteCookie("usr");
                }        
                
                if(reponse.redirige != undefined && reponse.redirige != ""){
                    document.location = reponse.redirige;
                    document.location.reload();
                } 
                else{
                    document.location.reload();
                }
        });

    
    return false;
    
}

$("#btGoLogin").click(getAuth);
$("#btUnLog").click(unLog);
$("#usr").focus();


});