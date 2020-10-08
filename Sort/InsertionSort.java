import java.io.*;
class test  
{
    public static void insertionSort(int[] a,int n){
        if (n<=1) return;
        for(int i=1;i<n;i++){
           int value = a[i]; //5 需要提前保存插入数的值
           int j=i-1;//6 同时发现j后面需要用到
           for(;j>=0;--j){//1 对第i个数都要从i-1到0做对比
                   //2 比第i个数大的都把它挪后，请注意，此时比较的是原来数组的第i个数，要用value，如果用a[i]<a[j]
		   //读取的是被覆盖后的值
		   if(value<a[j]){               
                    a[j+1] = a[j];
                }else{
                    break;//3 遇到第一个没能比第i个数大的数，就不用继续循环了，直接退出
                }
            } 
            //如果j自然脱离，此时的j为-1，否则j依然保留
            a[j+1] = value;//4 插在此时用来作比较的位置j的后面一位
        }
        
        return;
    }
    
	public static void main (String[] args) throws java.lang.Exception
	{
		int[] a = {6,5,4,1,2,3};
		insertionSort(a,a.length);
		for(int i=0;i<a.length;i++){
		    System.out.println(a[i]);
		}
	}
}
