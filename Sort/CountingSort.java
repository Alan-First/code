import java.io.*;
class test  
{
    public static int[] countingSort(int[] a,int n){
        int maxA = findMax(a);
        int[] b = new int[maxA+1];//b含有0~maxA这些元素，下标到maxA为止
        int[] c = new int[n];
        for(int i=0;i<b.length;i++){
            b[i]=0;
        }
        for(int i=0;i<n;i++){
            b[a[i]] +=1;
        }
        for(int i=1;i<b.length;i++){
            b[i]+=b[i-1];
            //System.out.println("b["+i+"]="+b[i]);
        }
        for(int i=0;i<n;i++){
            c[b[a[i]]-1]=a[i];
            b[a[i]]-=1;
        }
        
        
        return c;
    }

    public static int findMax(int[] a){
        int maxA = 0;
        int i=0;
        while(i<a.length){
            if(a[i]>maxA){
                maxA = a[i];
            }
            i++;
        }
        return maxA;
    }
    
    
	public static void main (String[] args) throws java.lang.Exception
	{
		int[] a = {6,5,4,1,2,3,0};//{1,2,3,7,3,3,8};//
		int[] c = countingSort(a,a.length);
		a=c;
		for(int i=0;i<a.length;i++){
		    System.out.println(a[i]);
		}
	}
}
