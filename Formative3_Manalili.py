#!/usr/bin/env python
# coding: utf-8

# In[83]:


def relationship_status(from_member, to_member, social_graph):
    if to_member in social_graph[from_member]["following"] and from_member in social_graph[to_member]["following"]:
        status="friends"
    elif to_member in social_graph[from_member]["following"]:
        status="follower"
    elif from_member in social_graph[to_member]["following"]:
        status="followed by"
    else:
        status="no relationship"
    return status
    
def tic_tac_toe(board):
    winner="NO WINNER"
    if len(board)==6:
        row_index=5
        column_index=5
        winner="NO WINNER"
        while row_index!=-1:
            if board[row_index][0]==board[row_index][1]==board[row_index][2]==board[row_index][3]==board[row_index][4]==board[row_index][5]:
                winner=board[row_index][0]
                break
            row_index-=1
        while column_index!=-1:
            if board[0][column_index]==board[1][column_index]==board[2][column_index]==board[3][column_index]==board[4][column_index]==board[5][column_index]:
                winner=board[column_index][0]
                break
            column_index-=1
        if board[5][0]==board[4][1]==board[3][2]==board[2][3]==board[1][4]==board[0][5]:
            winner=board[5][0]
        if board[0][0]==board[1][1]==board[2][2]==board[3][3]==board[4][4]==board[5][5]:
            winner=board[0][0]
    if len(board)==5:
        row_index=4
        column_index=4
        winner="NO WINNER"
        while row_index!=-1:
            if board[row_index][0]==board[row_index][1]==board[row_index][2]==board[row_index][3]==board[row_index][4]:
                winner=board[row_index][0]
                break
            row_index-=1
        while column_index!=-1:
            if board[0][column_index]==board[1][column_index]==board[2][column_index]==board[3][column_index]==board[4][column_index]:
                winner=board[0][column_index]
                break
            column_index-=1
        if board[4][0]==board[3][1]==board[2][2]==board[1][3]==board[0][4]:
            winner=board[4][0]
        if board[0][0]==board[1][1]==board[2][2]==board[3][3]==board[4][4]:
            winner=board[0][0]    
    if len(board)==4:
        row_index=3
        column_index=3
        winner="NO WINNER"
        while row_index!=-1:
            if board[row_index][0]==board[row_index][1]==board[row_index][2]==board[row_index][3]:
                winner=board[row_index][0]
                break
            row_index-=1
        while column_index!=-1:
            if board[0][column_index]==board[1][column_index]==board[2][column_index]==board[3][column_index]:
                winner=board[0][column_index]
                break
            column_index-=1
        if board[3][0]==board[2][1]==board[1][2]==board[0][3]:
            winner=board[3][0]
        if board[0][0]==board[1][1]==board[2][2]==board[3][3]:
            winner=board[0][0]
    if len(board)==3:
        row_index=2
        column_index=2
        winner="NO WINNER"
        while row_index!=-1:
            if board[row_index][0]==board[row_index][1]==board[row_index][2]:
                winner=board[row_index][0]
                break
            row_index-=1
        while column_index!=-1:
            if board[0][column_index]==board[1][column_index]==board[2][column_index]:
                winner=board[0][column_index]
                break
            column_index-=1
        if board[2][0]==board[1][1]==board[0][2]:
            winner=board[2][0]
        if board[0][0]==board[1][1]==board[2][2]:
            winner=board[0][0]
    if winner=="":
        winner="NO WINNER"
    return winner

def eta(first_stop,second_stop,route_map):
    inputted_route=(first_stop,second_stop)
    travel_time=0
    count_legs=0
    legs=()
    list_of_stops=()
    stop1=[]
    next_stop=[]
    travel_time1=0
    accumulated_travel_time=0
    first_stop_index=0
    next_stop_index=0
    number_of_succeeding_stops=1
    if inputted_route in route_map:
        travel_time=route_map[inputted_route]['travel_time_mins']
        return travel_time
    else:
        legs=list(route_map.keys())
        list_of_stops=list(route_map.items())
        while count_legs!=len(legs):
            if legs[count_legs][0]==first_stop:
                first_stop_index=count_legs
                break
            count_legs+=1
        stop1=list_of_stops[first_stop_index][1]
        travel_time1=stop1['travel_time_mins']
        while (first_stop_index+number_of_succeeding_stops)!=len(legs)+1:
            if first_stop_index+number_of_succeeding_stops==len(legs):
                first_stop_index=0
                number_of_succeeding_stops=0
            if legs[first_stop_index+number_of_succeeding_stops][1]!=second_stop:
                next_stop_index=first_stop_index+number_of_succeeding_stops
                next_stop=list_of_stops[next_stop_index][1]
                accumulated_travel_time+=next_stop['travel_time_mins']
            else:
                next_stop_index=first_stop_index+number_of_succeeding_stops
                next_stop=list_of_stops[next_stop_index][1]
                accumulated_travel_time+=next_stop['travel_time_mins']
                break
            number_of_succeeding_stops+=1  
        return travel_time1+accumulated_travel_time




# In[ ]:




