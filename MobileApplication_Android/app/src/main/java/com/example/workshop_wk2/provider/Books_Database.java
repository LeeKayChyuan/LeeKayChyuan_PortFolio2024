package com.example.workshop_wk2.provider;

import android.content.Context;

import androidx.room.Database;
import androidx.room.Room;
import androidx.room.RoomDatabase;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

@Database(entities = {Books_attribute.class}, version = 1)
public abstract class Books_Database extends RoomDatabase {
    public static final String BOOK_DATABASE_NAME = "Book_database";

    public abstract Books_Dao booksDao();

    // marking the instance as volatile to ensure atomic access to the variable
    private static volatile Books_Database INSTANCE;
    private static final int NUMBER_OF_THREADS = 4;
    static final ExecutorService databaseWriteExecutor =
            Executors.newFixedThreadPool(NUMBER_OF_THREADS);

    static Books_Database getDatabase(final Context context) {
        if (INSTANCE == null) {
            synchronized (Books_Database.class) {
                if (INSTANCE == null) {
                    INSTANCE = Room.databaseBuilder(context.getApplicationContext(),
                                    Books_Database.class, BOOK_DATABASE_NAME)
                            .build();
                }
            }
        }
        return INSTANCE;
    }
}
