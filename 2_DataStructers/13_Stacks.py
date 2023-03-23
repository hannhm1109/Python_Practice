#LIFO -> LAST IN FIRST OUT
browsing_session = []
browsing_session.append(1)
#To add an item on top of the stack
browsing_session.append(2)
browsing_session.append(3)
browsing_session[-1]
#We use it to get the item on top of  the stack 
print(browsing_session)
last = browsing_session.pop()
#To remove an item on top of the stack 
print(last)
print(browsing_session)
print("redirect", browsing_session)
#We check the stack if it's empty 
if not browsing_session:
    print("disable")