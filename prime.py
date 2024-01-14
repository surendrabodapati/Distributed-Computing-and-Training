#simple program to find the prime numbers between the given range

import sys
import time
import multiprocessing as mp

def prime(start , end):
    ans=0
    for i in range(max(2,start),end+1,1):
        count=0
        j=i-1
        while(not count and j>1):
            if i%j==0:
                count=1
                break
            j-=1
        
        if not count:
            ans+=1
    print("Number of prime numbers between the given range is ",ans)

if __name__ == "__main__":

    if len(sys.argv) == 3:
        start = time.time()
        prime( int( sys.argv[1] ) , int( sys.argv[2] ) )
        print("time taken to generate prime numbers ", time.time() - start)
    elif len( sys.argv ) == 4:
        start = time.time()
        
        with mp.Pool( processes = int( sys.argv[3] )) as pool:
            pool.starmap(prime, [(x, x + 1000) for x in range(int(sys.argv[1]), int(sys.argv[2]), 1000)])
 

        #prime( int( sys.argv[1] ) , int( sys.argv[2] ) )
        print("time taken to generate prime numbers with 16 cores ", time.time() - start)

