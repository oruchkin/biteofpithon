def solution(x, y):
    
    x_number = 0
    for i in range(1,x+1):
        x_number += i    
            
    print(f"x_number {x_number}")

    y_number = 0
    # if y < 2:
    #     return x_number
    
    for i in range(1,y):       
        
        y_number += (x-1) + i
    
    y_number += x_number
 
    print(f"y_number {y_number}")

solution(5,6)

#---  (3,4)
#---> x 6, y 18
    

# x = 1
# for y in range(1,10,1):      
#     print(f"{y}"*x)
#     for x in range(y):
#         x += 1

        
# def solution(x, y):

#     result = y

#     for i in range(1, x+1):
#         result += i

#     return result


# print(solution(5, 4))
