#include <stdio.h> 
#include <malloc.h>

typedef struct Tree         //建立二叉树的结构体
{
    int num;                //包含一个数字num,即存储的数据
    Tree *Lchild;           //左孩子,左孩子也是tree类型的,递归
    Tree *Rchild;           //定义右孩子
}Tree;

void tree_insert(Tree **p_this, int num)            //插入变量的函数
{
    Tree *p_new;                                    /*建立一个排序二叉树*/

    if(*p_this == NULL)                             //如果是空树
    {
        p_new = (Tree *)malloc(sizeof(Tree));       //为p_new开辟大小为tree的新空间
        p_new->num = num;                           //插入的num值给p_new->num,左右孩子为NULL
        p_new->Lchild = NULL;
        p_new->Rchild = NULL;
        *p_this = p_new;                            //p_this指向p_new的位置
    } 
    else                                            //如果不是空树
    {
        if(num < (*p_this)->num)                    //如果小于当前树的值,左向插入
        {
            tree_insert(&((*p_this)->Lchild), num); //递归调用tree_insert函数
        } 
        else if(num > (*p_this)->num)               //大于,右向插入
        {
            tree_insert(&((*p_this)->Rchild), num); //递归调用tree_insert函数
        }
    }
}

void DLR(Tree *p_this)              /*先序遍历*/
{//先序遍历的意思是先访问父树,然后左孩子,然后右孩子
    if(p_this != NULL)
    {
        printf("%3d", p_this->num); //先父树
        DLR(p_this->Lchild);        //左边
        DLR(p_this->Rchild);        //右边
    }
}

void LDR(Tree *p_this)              /*中序遍历，也即是顺序输出*/
{ //先左边,再父树,再右边
    if(p_this != NULL)
    {
        LDR(p_this->Lchild);        //递归输出左边
        printf("%3d", p_this->num); //父树
        LDR(p_this->Rchild);        //右边
    }
}

void LRD(Tree *p_this)              /*后序遍历*/
{//先左边,再右边,再父亲
    if(p_this != NULL)
    {
        LRD(p_this->Lchild);        //左边
        LRD(p_this->Rchild);        //右边
        printf("%3d", p_this->num); //父亲
    }
}

int main()                  //主函数
{
    int i = 0;              //i用来循环,gotton用来接收用户输入的数据
    int gotton = 0;
    Tree *head = NULL;      //head先为NULL

    for(i=1; i<=5; i++)     //循环5次而已
    {
        printf("please input the %d number:", i);     /*不能输入相同数据，小bug*/  //其实可以默认设置为如果两数相同,自动放在左边,tree_insert处没有考虑,所以有此问题
        scanf("%d", &gotton);           //输入gotton
        tree_insert(&head, gotton);     //从head开始插入gotton
    }

    printf("the preorder traversal is: ");  DLR(head);printf("\n");     //先序遍历
    printf("the inorder traversal is:  ");  LDR(head);printf("\n");     //中序遍历
    printf("the postorder traversal is:");  LRD(head);printf("\n");     //后续遍历

    getchar();              //保持屏幕
    getchar();              //保持屏幕

    return 0;
}