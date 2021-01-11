import random
import time

def field_print(field,count,location,state):
    if state == "탄생":
        print_state = "탄생"
    elif state == "적응기":
        print_state = "적응기"
    else:
        pass
    
    print("생명체 숫자 : ",count)
    print("상태 : ",print_state)
    
    for i in field:
        for j in range(len(field)):
            print(i[j],end='')
        print("\n")
    print("---------------------------------")
#    time.sleep(1)
       
def al_env(field,count,location):
    cnt = 0
    for i in location:#i[0]-> x축, i[1]->y축
        if i[0] == 0: #첫번째 줄
            if i[1] == 0:
                if (field[i[0]+1][i[1]] == '[O]') and (field[i[0]][i[1]+1] == '[O]'): #하,우
                    field[i[0]+1][i[1]] = '[ ]' #하
                    cnt = cnt + 1
                    
                    field[i[0]][i[1]+1] = '[ ]' #우
                    cnt = cnt + 1

            elif i[1] == 9:
                if (field[i[0]+1][i[1]] == '[O]') and (field[i[0]][i[1]-1] == '[O]'):  #하,좌
                    field[i[0]+1][i[1]] = '[ ]' #하
                    cnt = cnt + 1
                    
                    field[i[0]][i[1]-1] = '[ ]'#좌
                    cnt = cnt + 1
                
            else:
                if (field[i[0]+1][i[1]] == '[O]')and(field[i[0]][i[1]-1] == '[O]')and(field[i[0]][i[1]+1] == '[O]'):
                    field[i[0]+1][i[1]] = '[ ]'#하
                    cnt = cnt + 1
                    
                    field[i[0]][i[1]-1] = '[ ]'#좌
                    cnt = cnt + 1
                    
                    field[i[0]][i[1]+1] = '[ ]'#우
                    cnt = cnt + 1
                
        elif i[0] == 9:#마지막 줄
            if i[1] == 0:
                if (field[i[0]-1][i[1]] == '[O]')and(field[i[0]][i[1]+1] == '[O]'):
                    field[i[0]-1][i[1]] = '[ ]'#상
                    cnt = cnt + 1

                    field[i[0]][i[1]+1] = '[ ]'#우
                    cnt = cnt + 1

            elif i[1] == 9:
                if (field[i[0]-1][i[1]] == '[O]')and(field[i[0]][i[1]-1] == '[O]'):
                    field[i[0]-1][i[1]] = '[ ]'#상
                    cnt = cnt + 1

                    field[i[0]][i[1]-1] = '[ ]'#좌
                    cnt = cnt + 1

            else:
                if (field[i[0]-1][i[1]] == '[O]')and(field[i[0]][i[1]-1] == '[O]')and(field[i[0]][i[1]+1] == '[O]'):
                    field[i[0]-1][i[1]] = '[ ]'#상
                    cnt = cnt + 1

                    field[i[0]][i[1]-1] = '[ ]'#좌
                    cnt = cnt + 1

                    field[i[0]][i[1]+1] = '[ ]'#우
                    cnt = cnt + 1
            
        else: #첫번쨰, 마지막 줄 제외한 모든 줄
            if i[1] == 0:
                if (field[i[0]-1][i[1]] == '[O]')and(field[i[0]+1][i[1]] == '[O]')and(field[i[0]][i[1]+1] == '[O]'):
                    field[i[0]-1][i[1]] = '[ ]'#상
                    cnt = cnt + 1
 
                    field[i[0]+1][i[1]] = '[ ]'#하
                    cnt = cnt + 1

                    field[i[0]][i[1]+1] = '[ ]'#우
                    cnt = cnt + 1
                    
            elif i[1] == 9:
                if (field[i[0]-1][i[1]] == '[O]')and(field[i[0]+1][i[1]] == '[O]')and(field[i[0]][i[1]-1] == '[O]'):
                    field[i[0]-1][i[1]] = '[ ]'#상
                    cnt = cnt + 1
                    
                    field[i[0]+1][i[1]] = '[ ]'#하
                    cnt = cnt + 1
                    
                    field[i[0]][i[1]-1] = '[ ]'#좌
                    cnt = cnt + 1
                    
            else:
                if (field[i[0]-1][i[1]] == '[O]')and(field[i[0]+1][i[1]] == '[O]')and(field[i[0]][i[1]-1] == '[O]')and(field[i[0]][i[1]+1] == '[O]'):
                    field[i[0]-1][i[1]] = '[ ]'#상
                    cnt = cnt + 1

                    field[i[0]+1][i[1]] = '[ ]'#하
                    cnt = cnt + 1
    
                    field[i[0]][i[1]-1] = '[ ]'#좌
                    cnt = cnt + 1

                    field[i[0]][i[1]+1] = '[ ]'#우
                    cnt = cnt + 1

#    for i in range(len(field)):
#        for j in range(len(field)):
#            if field[i][j] == '[O]':
#                tmp = (i,j)
#                location.append(tmp)
#    print(location)
        
    count = count - cnt           
    return field,count

def al_check(field,count,location):
    cnt = 0
    for i in location:#i[0]-> x축, i[1]->y축
        if i[0] == 0: #첫번째 줄
            if i[1] == 0:
                if (field[i[0]+1][i[1]] == '[O]') and (field[i[0]][i[1]+1] == '[O]'): #하,우
                    field[i[0]][i[1]] = '[ ]' 
                    cnt = cnt + 1

            elif i[1] == 9:
                if (field[i[0]+1][i[1]] == '[O]') and (field[i[0]][i[1]-1] == '[O]'):  #하,좌
                    field[i[0]][i[1]] = '[ ]' 
                    cnt = cnt + 1
                
            else:
                if (field[i[0]+1][i[1]] == '[O]')and(field[i[0]][i[1]-1] == '[O]')and(field[i[0]][i[1]+1] == '[O]'):
                    field[i[0]][i[1]] = '[ ]' 
                    cnt = cnt + 1
                
        elif i[0] == 9:#마지막 줄
            if i[1] == 0:
                if (field[i[0]-1][i[1]] == '[O]')and(field[i[0]][i[1]+1] == '[O]'):
                    field[i[0]][i[1]] = '[ ]' 
                    cnt = cnt + 1

            elif i[1] == 9:
                if (field[i[0]-1][i[1]] == '[O]')and(field[i[0]][i[1]-1] == '[O]'):
                    field[i[0]][i[1]] = '[ ]' 
                    cnt = cnt + 1

            else:
                if (field[i[0]-1][i[1]] == '[O]')and(field[i[0]][i[1]-1] == '[O]')and(field[i[0]][i[1]+1] == '[O]'):
                    field[i[0]][i[1]] = '[ ]' 
                    cnt = cnt + 1
            
        else: #첫번쨰, 마지막 줄 제외한 모든 줄
            if i[1] == 0:
                if (field[i[0]-1][i[1]] == '[O]')and(field[i[0]+1][i[1]] == '[O]')and(field[i[0]][i[1]+1] == '[O]'):
                    field[i[0]][i[1]] = '[ ]' 
                    cnt = cnt + 1
                    
            elif i[1] == 9:
                if (field[i[0]-1][i[1]] == '[O]')and(field[i[0]+1][i[1]] == '[O]')and(field[i[0]][i[1]-1] == '[O]'):
                    field[i[0]][i[1]] = '[ ]' 
                    cnt = cnt + 1
                    
            else:
                if (field[i[0]-1][i[1]] == '[O]')and(field[i[0]+1][i[1]] == '[O]')and(field[i[0]][i[1]-1] == '[O]')and(field[i[0]][i[1]+1] == '[O]'):
                    field[i[0]][i[1]] = '[ ]' 
                    cnt = cnt + 1

#    for i in range(len(field)):
#        for j in range(len(field)):
#            if field[i][j] == '[O]':
#                tmp = (i,j)
#                location.append(tmp)
#    print(location)
        
    count = count - cnt           
    return field,count            
    
field = [['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]'],
         ['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]'],
         ['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]'],
         ['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]'],
         ['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]'],
         ['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]'],
         ['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]'],
         ['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]'],
         ['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]'],
         ['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]']]

x_axis = [0,1,2,3,4,5,6,7,8,9]
y_axis = [0,1,2,3,4,5,6,7,8,9]
location = []
count = 0

for i in range(10):
    x = random.choice(x_axis) #랜덤하게 생명체 생성
    y = random.choice(y_axis)

    field[x][y] = '[O]'
    count = count +1

    tmp_x_y = [x,y]
    location.append(tmp_x_y) #새롭게 생긴 생명체 위치 저장
    
    state = "탄생"
    field_print(field,count,location,state)

    check= al_check(field,count,location) #주변에 생명체 없을 경우 새로운 생명체 생성
    count = check[1]
    time.sleep(3)

    state = "적응기"
    field_print(check[0],check[1],location,state)
    time.sleep(3)



