from flask import Flask, render_template, request, redirect, url_for
import json 

app = Flask(__name__)
filename="/workspaces/Test_Setup/library.json"

def update_library():
    library_data=[]
    try:
          with open(filename, 'r') as file:
              # Load the data from the file
              library_data = json.load(file)
              # Print the data
              # print(json.dumps(library_data, indent=4))
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
    except json.JSONDecodeError:
        print(f"The file {filename} could not be decoded.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return library_data

@app.route('/add_books_page')
def add_books_page():
    return render_template('add_books.html') 

@app.route('/')
def display_books_page():
    # Load data from JSON file
    library_data = update_library()
    print(library_data)
    # Send data to template
    return render_template('display_books.html', data={"library": library_data})


@app.route('/add_book_form', methods=['POST'])
def add_book_form():
    book = {
        "book_title": request.form['book_title'],
        "author": request.form['author'],
        "publisher": request.form['publisher'],
        "genre": request.form['genre'],
        "type": request.form['type'],
        "ISBN": request.form['ISBN'],
        "quantity_remaining": int(request.form['quantity_remaining'])
    }
    library_data = update_library()
    library_data.append(book)
    
    with open(filename, "w") as file:
        json.dump(library_data, file, indent=4)

    # Redirect to the add_book_form page to clear the form
    return redirect(url_for('add_books_page'))

@app.route('/edit_book_form', methods=['POST'])
def update_book_form():
    old_book = json.loads(request.form['book_object'])
    book = {
        "book_title": request.form['book_title'],
        "author": request.form['author'],
        "publisher": request.form['publisher'],
        "genre": request.form['genre'],
        "type": request.form['type'],
        "ISBN": request.form['ISBN'],
        "quantity_remaining": int(request.form['quantity_remaining'])
    }
    #load library data
    library_data = update_library()
    #remove old_book from library data
    library_data = [book for book in library_data if book['ISBN'] != old_book['ISBN']]
    #add new book to library data
    library_data.append(book)
    #save library data to json file
    with open(filename, "w") as file:
        json.dump(library_data, file, indent=4)
    
    return redirect(url_for('display_books_page'))

@app.route('/remove_book', methods=['POST'])
def remove_book():
    book_to_remove = json.loads(request.form['book_object'])

    # Load library data
    library_data=update_library()

    # Remove the book from library data
    library_data = [book for book in library_data if book['ISBN'] != book_to_remove['ISBN']]

    # Save the updated library data
    with open(filename, 'w') as file:
        json.dump(library_data, file, indent=4)

    return redirect(url_for('display_books_page'))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5001)
