#include <stdio.h> 
#include <malloc.h>

typedef struct Tree         //建立二叉树的结构体
{
    int num;                //包含一个数字num,即存储的数据
    Tree *Lchild;           //左孩子,左孩子也是tree类型的,递归
    Tree *Rchild;           //定义右孩子
}Tree;

void insert(Tree **p0,int x) //插入变量的函数,类型是tree,就像int *insert()一样,差不多的意思
{
    Tree *p1;                       /*建立一个排序二叉树*/

    if(*p0==NULL)                   //如果是空树
    { 

        p1=(Tree *)malloc(sizeof(Tree));                //为p1开辟大小为tree的新空间
        p1->num=x;p1->Lchild=NULL;p1->Rchild=NULL;      //插入的x值给p1->num,左右孩子为NULL
        *p0=p1;                                         //p0指向P1的位置
    } 
    else                                    //如果不是空树
    {
        if(x<(*p0)->num)                    //如果小于当前树的值,左向插入
        {
            insert(&((*p0)->Lchild),x);     //递归调用insert函数
        } 
        else if(x>(*p0)->num)               //大于,右向插入
        {
            insert(&((*p0)->Rchild),x);     //递归调用insert函数
        }
    }
}

void DLR(Tree *p0)              /*先序遍历*/
{//先序遍历的意思是先访问父树,然后左孩子,然后右孩子
    if(p0!=NULL)
    {
        printf("%3d",p0->num);  //先父树
        DLR(p0->Lchild);        //左边
        DLR(p0->Rchild);        //右边
    }
}

void LDR(Tree *p0)              /*中序遍历，也即是顺序输出*/
{ //先左边,再父树,再右边
    if(p0!=NULL)
    {
        LDR(p0->Lchild);        //递归输出左边
        printf("%3d",p0->num);  //父树
        LDR(p0->Rchild);        //右边
    }
}

void LRD(Tree *p0)              /*后序遍历*/
{//先左边,再右边,再父亲
    if(p0!=NULL)
    {
        LRD(p0->Lchild);        //左边
        LRD(p0->Rchild);        //右边
        printf("%3d",p0->num);  //父亲
    }
}

int main()                  //主函数
{
    int i=0,x=0;            //i用来循环,x用来接收用户输入的数据
    Tree *head=NULL;        //head先为NULL

    for(i=1;i<=5;i++)       //循环5次而已
    {
        printf("please input the %d number:",i);     /*不能输入相同数据，小bug*/  //其实可以默认设置为如果两数相同,自动放在左边,insert处没有考虑,所以有此问题
        scanf("%d",&x);     //输入x
        insert(&head,x);    //从head开始插入x
    }

    printf("the preorder traversal is: ");  DLR(head);printf("\n");     //先序遍历
    printf("the inorder traversal is:  ");  LDR(head);printf("\n");     //中序遍历
    printf("the postorder traversal is:");  LRD(head);printf("\n");     //后续遍历

    getchar();              //保持屏幕
    getchar();              //保持屏幕

    return 0;
}