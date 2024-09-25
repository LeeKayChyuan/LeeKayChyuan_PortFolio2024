package com.example.workshop_wk2;

import androidx.annotation.NonNull;
import androidx.appcompat.app.ActionBarDrawerToggle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.drawerlayout.widget.DrawerLayout;
import androidx.lifecycle.ViewModelProvider;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.MotionEvent;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.Toast;

import com.example.workshop_wk2.provider.Books_Repository;
import com.example.workshop_wk2.provider.Books_ViewModel;
import com.example.workshop_wk2.provider.Books_attribute;
import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.android.material.navigation.NavigationView;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

import java.util.ArrayList;


public class MainActivity extends AppCompatActivity {
    EditText ETBookName;
    EditText ETTitle;
    EditText ETIsbn;
    EditText ETAuthor;
    EditText ETDescription;
    EditText ETPrice;

    //ListView initialise
    ArrayList<String> myList = new ArrayList<>();
    ArrayAdapter<String> myAdapter;
    DrawerLayout drawerLayout;

    //recycle view declaration
    ArrayList<Books_attribute> mydata = new ArrayList<>();

    private Books_ViewModel mBooksViewModel;

    DatabaseReference myRef;

    View TouchFrame;
    int initial_x;
    int initial_y;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.drawer_layout);

        ETBookName = findViewById(R.id.ID1);
        ETTitle = findViewById(R.id.Title1);
        ETIsbn = findViewById(R.id.ISBN1);
        ETAuthor = findViewById(R.id.Author1);
        ETDescription = findViewById(R.id.Description1);
        ETPrice = findViewById(R.id.Price1);

        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        //FAB
        FloatingActionButton FAB = findViewById(R.id.floatingActionButton4);
        FAB.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                addBook_rv();
            }
        });

        //Navigation view button
        drawerLayout = findViewById(R.id.dl);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawerLayout, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawerLayout.addDrawerListener(toggle);
        toggle.syncState();

        //instance for navigation view
        NavigationView navigationView = findViewById(R.id.navigation_view);
        navigationView.setNavigationItemSelectedListener(new MyDrawerListener());

        //wk7
        mBooksViewModel = new ViewModelProvider(this).get(Books_ViewModel.class);
        mBooksViewModel.getAllItems().observe(this, newData -> {
        });

        getSupportFragmentManager().beginTransaction().replace(R.id.frame1,new RecyclerViewFragment()).commit();

        // Write a message to the database
        FirebaseDatabase database = FirebaseDatabase.getInstance("https://workshop-wk8-default-rtdb.asia-southeast1.firebasedatabase.app/");
        myRef = database.getReference("books/myBook");

        //Touch Gestures
        TouchFrame = findViewById(R.id.touchFrame);

        TouchFrame.setOnTouchListener(new View.OnTouchListener() {
            @Override
            public boolean onTouch(View view, MotionEvent event) {

                int motion = event.getActionMasked();

                switch(motion){
                    case(MotionEvent.ACTION_DOWN):
                        initial_x = (int)event.getX();
                        initial_y = (int)event.getY();

                        if(initial_y < 100 && initial_x < 100) {
                            ETAuthor.setText(ETAuthor.getText().toString().toUpperCase());
                        }
                        return true;

                    case(MotionEvent.ACTION_MOVE):
                        if(Math.abs(initial_y - event.getY()) < 25){
                            if(initial_x < event.getX()){
                                int BookPrice = Integer.parseInt(ETPrice.getText().toString());
                                BookPrice += 1;
                                ETPrice.setText(BookPrice + "");
                            }
                        }
                        return true;

                    case(MotionEvent.ACTION_UP):
                        if(Math.abs(initial_y - event.getY()) < 25){
                            if(initial_x > event.getX()){
                                addBook_rv();
                            }
                        }
                        else if(Math.abs(initial_x - event.getX()) < 25){
                            if(initial_y > event.getY()){
                                ClearField1();
                            }
                            else if(initial_y < event.getY()){
                                finish();
                            }
                        }
                        return true;

                    default:
                        return false;
                }
            }
        });
    }

    public void ClearField1() {
        //clear text view
        ETBookName.setText("");
        ETTitle.setText("");
        ETIsbn.setText("");
        ETAuthor.setText("");
        ETDescription.setText("");
        ETPrice.setText("");
    }

    protected void onSaveInstanceState(@NonNull Bundle outState) {
        super.onSaveInstanceState(outState); //*auto save everything
    }

    protected void onRestoreInstanceState(@NonNull Bundle savedInstanceState) {
        super.onRestoreInstanceState(savedInstanceState);
    }

    protected void onStart() {
        super.onStart();

        loadAttribute();
    }

    protected void onStop() {
        super.onStop();

        saveAttribute();
    }

    public void saveAttribute() {
        //save the attribute into shared preferences
        SharedPreferences mySharedPreferences = getSharedPreferences("workshop",0);
        SharedPreferences.Editor myESPEditor = mySharedPreferences.edit();

        myESPEditor.putString("name", ETBookName.getText().toString());
        myESPEditor.putString("title", ETTitle.getText().toString());
        myESPEditor.putString("isbn", ETIsbn.getText().toString());
        myESPEditor.putString("author", ETAuthor.getText().toString());
        myESPEditor.putString("description", ETDescription.getText().toString());
        myESPEditor.putString("price", ETPrice.getText().toString());
        myESPEditor.apply();
    }

    public void loadAttribute() {
        //load the attribute from Shared Preferences
        SharedPreferences mySharedPreferences = getSharedPreferences("workshop",0);

        ETBookName.setText(mySharedPreferences.getString("name",""));
        ETTitle.setText(mySharedPreferences.getString("title", ""));
        ETIsbn.setText(mySharedPreferences.getString("isbn",""));
        ETAuthor.setText(mySharedPreferences.getString("author",""));
        ETDescription.setText(mySharedPreferences.getString("description",""));
        ETPrice.setText(mySharedPreferences.getString("price",""));
    }

//wk5
    //navigation view
    class MyDrawerListener implements NavigationView.OnNavigationItemSelectedListener{
        @Override
        public boolean onNavigationItemSelected(@NonNull MenuItem item) {
            // get the id of the selected item
            int id = item.getItemId();

            if (id == R.id.drawer_addbook) {
                addBook_rv();
            }
            else if (id == R.id.drawer_RemoveLast) {
                mBooksViewModel.deleteLastBook();
            }
            else if (id == R.id.drawer_RemoveAll) {
                mBooksViewModel.deleteAll();
                myRef.removeValue();
            }
            else if (id == R.id.ListAll){
                showList();
            }
            else if (id == R.id.drawer_Close){
                finish();
            }
            // close the drawer
            drawerLayout.closeDrawers();
            // tell the OS
            return true;
        }
    }

    //option menu
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        //inflate option_menu and hook it to the toolbar(3dots icon)
        getMenuInflater().inflate(R.menu.option_menu,menu);
        return super.onCreateOptionsMenu(menu);
    }

    @Override
    public boolean onOptionsItemSelected(@NonNull MenuItem item) {
        int id = item.getItemId();

        if (id == R.id.option_clear) {
            ClearField1();
        }
        else if (id == R.id.option_load) {
            loadAttribute();
        }
        else if (id == R.id.DeletePrice){
            mBooksViewModel.deletePrice50();
        }

        // close the drawer
        drawerLayout.closeDrawers();
        // tell the OS
        return super.onOptionsItemSelected(item);
    }

//wk6
    public void setAttribute() {
        String BookTitle = ETTitle.getText().toString();
        String BooKISBN = ETIsbn.getText().toString();
        String BookAuthor = ETAuthor.getText().toString();
        String BookDesc = ETDescription.getText().toString();
        int BookPrice = Integer.parseInt(ETPrice.getText().toString());

        Books_attribute MyBook = new Books_attribute(BookTitle, BooKISBN, BookAuthor, BookDesc, BookPrice);
        mydata.add(MyBook);

        mBooksViewModel.insert(MyBook);
        myRef.push().setValue(MyBook);
    }
    public void addBook_rv() {
        setAttribute();
        saveAttribute();
    }

    public void showList() {
        Intent i = new Intent(this, Main2Activity.class);
        startActivity(i);
    }
}