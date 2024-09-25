package com.example.workshop_wk2.provider;

import androidx.lifecycle.LiveData;
import androidx.room.Dao;
import androidx.room.Insert;
import androidx.room.Query;

import java.util.List;

@Dao
public interface Books_Dao {
    @Query("select * from books")
    LiveData<List<Books_attribute>> getAllBook();

    @Query("select * from books where BooksTitle=:name")
    List<Books_attribute> getBook(String name);

    @Insert
    void addBooks(Books_attribute books);

    @Query("delete from books where BooksTitle= :name")
    void deleteBooks(String name);

    @Query("delete FROM books")
    void deleteAllBooks();

    @Query("Delete From Books Where BooksID =(SELECT MAX(BooksId) From Books)")
    void deleteLastBooks();

    @Query("Delete From Books Where BooksPrice > 50")
    void deletePrice50();
}
