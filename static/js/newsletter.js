$(document).ready(function(){
    $('form').submit(function(event){
      event.preventDefault()
      form = $('form')

      $.ajax({
          type: "POST",
          url: "/ajax/newsletter/",
          data: form.serialize(),
          dataType: "json",
          success: function (data) {
              alert(data['success'])
          },
      })
     $('#id_email').val('')
    }) 
  
  }) 