package com.example.workshop_wk2.provider;

import androidx.annotation.NonNull;
import androidx.room.ColumnInfo;
import androidx.room.Entity;
import androidx.room.PrimaryKey;

@Entity(tableName = "books")
public class Books_attribute {

    @PrimaryKey(autoGenerate = true)
    @NonNull
    @ColumnInfo(name = "BooksID")
    int Book_ID;

    @ColumnInfo(name = "BooksTitle")
    String Book_Title;

    @ColumnInfo(name = "BooksISBN")
    String Book_ISBN;

    @ColumnInfo(name = "BooksAuthor")
    String Book_Author;

    @ColumnInfo(name = "BooksDesc")
    String Book_Desc;

    @ColumnInfo(name = "BooksPrice")
    int Book_Price;

    public Books_attribute(String Book_Title, String Book_ISBN, String Book_Author, String Book_Desc, int Book_Price) {
        this.Book_Title = Book_Title;
        this.Book_ISBN = Book_ISBN;
        this.Book_Author = Book_Author;
        this.Book_Desc = Book_Desc;
        this.Book_Price = Book_Price;
    }

    public int getBook_ID() {
        return Book_ID;
    }

    public void setBook_ID(int book_Name) {
        Book_ID = book_Name;
    }

    public String getBook_Title() {
        return Book_Title;
    }

    public void setBook_Title(String book_Title) {
        Book_Title = book_Title;
    }

    public String getBook_ISBN() {
        return Book_ISBN;
    }

    public void setBook_ISBN(String book_ISBN) {
        Book_ISBN = book_ISBN;
    }

    public String getBook_Author() {
        return Book_Author;
    }

    public void setBook_Author(String book_Author) {
        Book_Author = book_Author;
    }

    public String getBook_Desc() {
        return Book_Desc;
    }

    public void setBook_Desc(String book_Desc) {
        Book_Desc = book_Desc;
    }

    public int getBook_Price() {
        return Book_Price;
    }

    public void setBook_Price(int book_Price) {
        Book_Price = book_Price;
    }

}
