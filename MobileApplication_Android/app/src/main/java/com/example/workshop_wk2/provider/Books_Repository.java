package com.example.workshop_wk2.provider;

import android.app.Application;

import androidx.lifecycle.LiveData;

import java.util.List;

public class Books_Repository {
    private Books_Dao mBooksDao;
    private LiveData<List<Books_attribute>> mAllBooks;

    Books_Repository(Application application) {
        Books_Database db = Books_Database.getDatabase(application);
        mBooksDao = db.booksDao();
        mAllBooks = mBooksDao.getAllBook();
    }

    LiveData<List<Books_attribute>> getAllItems() {
        return mAllBooks;
    }

    void insert(Books_attribute books) {
        Books_Database.databaseWriteExecutor.execute(() -> mBooksDao.addBooks(books));
    }

    void deleteAll(){
        Books_Database.databaseWriteExecutor.execute(()->{
            mBooksDao.deleteAllBooks();
        });
    }

    void deleteLastBook(){
        Books_Database.databaseWriteExecutor.execute(()->{
            mBooksDao.deleteLastBooks();
        });
    }

    void deletePrice50(){
        Books_Database.databaseWriteExecutor.execute(()->{
            mBooksDao.deletePrice50();
        });
    }
}
