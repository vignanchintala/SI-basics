#YET TO BE SOLVED

'''
Print right-angled triangle pattern. See example for more details.

Input Format

First line of input contains a single integer N - the size of the triangle.

Constraints

1 <= N <= 50

Output Format

For the given integer, print the right-angled triangle pattern.

Sample Input 0

5
Sample Output 0

1
2 6
3 7 10
4 8 11 13
5 9 12 14 15
Explanation 0

Self Explanatory
'''

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    int n,count;
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        count=i+1;
        for(int j=0;j<=i;j++)
        {
            printf("%d ",count);
            count= count + n-j - 1;
        }
        printf("\n");
    }
    return 0;
}
