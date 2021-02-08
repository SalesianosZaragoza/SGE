import { LightningElement, track } from 'lwc';

export default class Library extends LightningElement {

 @track title;
 @track isbn;
 @track books;
    constructor(){
        books = []

    }

    handleBook(event){
        book = { title: this.title, isbn: this.isbn   }
        this.books.push(book)
    }

    isBookListEmpty(){
        return this.books.length === 0
    }
}