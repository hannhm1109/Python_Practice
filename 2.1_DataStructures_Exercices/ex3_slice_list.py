sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

lenght = len(sample_list) 

chunk_size = int(lenght / 3)

start = 0
end = chunk_size

for i in range(3):
    #Get indexes
    indexes = slice(start , end)

    #Get chunk
    list_chunk = sample_list[indexes]
    print("chunk ", i, list_chunk)

    #Reverse chunk
    print("After reversing it ",list(reversed(list_chunk)))

    start = end
    end += chunk_size
