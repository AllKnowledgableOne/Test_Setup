function closeModal(){
    document.getElementById("editModal").style.display = "none";
  }
  
  function changeQuantity(x){
    var quantity_remaining=document.getElementById("quantity_remaining").value;
    quantity_remaining=parseInt(quantity_remaining);
    quantity_remaining+=x;
    document.getElementById("quantity_remaining").value=quantity_remaining;
  }
  
  
  function removeBook() {
  
    // Optional: Confirm with the user that they want to remove the book
    var confirmRemoval = confirm("Are you sure you want to remove this book?");
    if (confirmRemoval) {
  
      // Close the modal
      closeModal();
      // Create a form element to submit the data
      var form = document.createElement('form');
      form.method = 'POST';
      form.action = '/remove_book';
  
      // Append the book_object input to the form
      var bookObjectInput = document.getElementById('book_object');
      form.appendChild(bookObjectInput.cloneNode());
  
      // Append the form to the body and submit it
      document.body.appendChild(form);
      form.submit();
    }
  }
  
  function openModal(e,row){
    // console.log(row.getData());
    var rowData = row.getData();
    document.getElementById("book_title").value = rowData.book_title;
    document.getElementById("author").value = rowData.author;
    document.getElementById("publisher").value = rowData.publisher;
    document.getElementById("genre").value = rowData.genre;
    document.getElementById(rowData.type == "Fiction" ? "fiction" : "non_fiction").checked = true;
    document.getElementById("ISBN").value = rowData.ISBN;
    document.getElementById("quantity_remaining").value = rowData.quantity_remaining;
  
  
    document.getElementById("book_object").value = JSON.stringify(rowData);//This saves a version of the book to be removed from the library if an edit occurs
    
    document.getElementById("editModal").style.display = "block";
  }