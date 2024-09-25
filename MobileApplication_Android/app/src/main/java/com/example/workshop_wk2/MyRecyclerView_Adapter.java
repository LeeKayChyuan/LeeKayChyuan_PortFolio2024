package com.example.workshop_wk2;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.example.workshop_wk2.provider.Books_attribute;

import java.util.ArrayList;
import java.util.List;

public class MyRecyclerView_Adapter extends RecyclerView.Adapter<MyRecyclerView_Adapter.ViewHolder>{
    List<Books_attribute> data = new ArrayList<>();

    public MyRecyclerView_Adapter(){

    }

    public void setData(List<Books_attribute> data) {
        this.data = data;
    }

    @NonNull
    @Override
    public MyRecyclerView_Adapter.ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View v = LayoutInflater.from(parent.getContext()).inflate(R.layout.recycleview,parent,false);
        ViewHolder viewHolder = new ViewHolder(v);
        return viewHolder;
    }

    @Override
    public void onBindViewHolder(@NonNull MyRecyclerView_Adapter.ViewHolder holder, int position) {
        holder.RVID.setText(data.get(position).getBook_ID() + "");
        holder.RVTitle.setText(data.get(position).getBook_Title());
        holder.RVISBN.setText(data.get(position).getBook_ISBN());
        holder.RVAuthor.setText(data.get(position).getBook_Author());
        holder.RVDescription.setText(data.get(position).getBook_Desc());
        holder.RVPrice.setText(data.get(position).getBook_Price() + "");
        holder.RVIndex.setText(String.valueOf(position));
    }

    @Override
    public int getItemCount() {
        return data.size();
    }

    //get view item from recycle view
    public class ViewHolder extends RecyclerView.ViewHolder{
        public TextView RVID,RVTitle,RVISBN,RVAuthor,RVDescription,RVPrice,RVIndex;

        public ViewHolder(@NonNull View itemView){
            super(itemView);
            RVID = itemView.findViewById(R.id.rv_id);
            RVTitle = itemView.findViewById(R.id.rv_title);
            RVISBN = itemView.findViewById(R.id.rv_isbn);
            RVAuthor = itemView.findViewById(R.id.rv_author);
            RVDescription = itemView.findViewById(R.id.rv_description);
            RVPrice =itemView.findViewById(R.id.rv_price);
            RVIndex =itemView.findViewById(R.id.rv_number2);
        }
    }
}
