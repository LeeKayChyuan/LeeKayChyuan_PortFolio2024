package com.example.workshop_wk2.provider;

import android.app.Application;

import androidx.annotation.NonNull;
import androidx.lifecycle.AndroidViewModel;
import androidx.lifecycle.LiveData;

import java.util.List;

public class Books_ViewModel extends AndroidViewModel {
    private Books_Repository mRepository;
    private LiveData<List<Books_attribute>> mAllBooks;

    public Books_ViewModel(@NonNull Application application) {
        super(application);
        mRepository = new Books_Repository(application);
        mAllBooks = mRepository.getAllItems();
    }

    public LiveData<List<Books_attribute>> getAllItems() {
        return mAllBooks;
    }

    public void insert(Books_attribute books) {
        mRepository.insert(books);
    }

    public void deleteAll(){
        mRepository.deleteAll();
    }

    public void deleteLastBook() {
        mRepository.deleteLastBook();
    }

    public void deletePrice50() {
        mRepository.deletePrice50();
    }
}
