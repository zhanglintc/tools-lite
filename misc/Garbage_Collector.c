/**************************************
 Refer to:
 http://blog.jobbole.com/53376/
**************************************/

#include <stdio.h>
#include <stdlib.h>

#define STACK_MAX 256

/***************************
 flag of types
***************************/
typedef enum
{
  OBJ_INT,
  OBJ_PAIR
} ObjectType;

/***************************
 definition of object
***************************/
typedef struct sObject
{
  ObjectType type;
  unsigned char marked;

  /* The next object in the linked list of heap allocated objects. */
  struct sObject* next;

  union
  {
    /* OBJ_INT */
    int value;

    /* OBJ_PAIR */
    struct
    {
      struct sObject* head;
      struct sObject* tail;
    };
  };
} Object;

/***************************
 definition of Virtual Machine
***************************/
typedef struct
{
  Object* stack[STACK_MAX];
  int stackSize;

  /* The first object in the linked list of all objects on the heap. */
  Object* firstObject;

  /* The total number of currently allocated objects. */
  int numObjects;

  /* The number of objects required to trigger a GC. */
  int maxObjects;
} VM;

/***************************
 print error messages
***************************/
void assert(int condition, const char* message)
{
  if (!condition)
  {
    printf("%s\n", message);
    exit(1);
  }
}

/***************************
 return a new Virtual Machine
***************************/
VM* newVM()
{
  VM* vm = (VM*)malloc(sizeof(VM));
  vm->stackSize = 0;
  vm->firstObject = NULL;
  vm->numObjects = 0;
  vm->maxObjects = 8;
  return vm;
}

/***************************
 push a object to a Virtual Machine
***************************/
void push(VM* vm, Object* value)
{
  assert(vm->stackSize < STACK_MAX, "Stack overflow!");
  vm->stack[vm->stackSize++] = value;
}

/***************************
 pop a 'thing' from a Virtual Machine
***************************/
Object* pop(VM* vm)
{
  assert(vm->stackSize > 0, "Stack underflow!");
  return vm->stack[--vm->stackSize];
}

/***************************
 mark a object as in-use
 1 for in-use
 0 for not-in-use
***************************/
void mark(Object* object)
{
  /* If already marked, we're done. Check this first to avoid recursing
     on cycles in the object graph. */
  if (object->marked) return;

  object->marked = 1;

  if (object->type == OBJ_PAIR)
  {
    mark(object->head);
    mark(object->tail);
  }
}

/***************************
 mark all objects in Virtual Machine
***************************/
void markAll(VM* vm)
{
  for (int i = 0; i < vm->stackSize; i++)
  {
    mark(vm->stack[i]);
  }
}

/***************************
 sweep the VM, check if there is
 object need to be removed
***************************/
void sweep(VM* vm)
{
  Object** object = &vm->firstObject;
  while (*object)
  {
    if (!(*object)->marked)
    {
      /* This object wasn't reached, so remove it from the list and free it. */
      Object* unreached = *object;

      *object = unreached->next;
      free(unreached);

      vm->numObjects--;
    }
    else
    {
      /* This object was reached, so unmark it (for the next GC) and move on to
       the next. */
      (*object)->marked = 0;
      object = &(*object)->next;
    }
  }
}

/***************************
 Garbage Collector
***************************/
void gc(VM* vm)
{
  int numObjects = vm->numObjects;

  markAll(vm);
  sweep(vm);

  vm->maxObjects = vm->numObjects * 2;

  printf("Collected %d objects, %d remaining.\n", 
         numObjects - vm->numObjects,
         vm->numObjects);
}

/***************************
 return a new object
***************************/
Object* newObject(VM* vm, ObjectType type) {
  if (vm->numObjects == vm->maxObjects) gc(vm);

  Object* object = (Object*)malloc(sizeof(Object));
  object->type = type;
  object->next = vm->firstObject;
  vm->firstObject = object;
  object->marked = 0;

  vm->numObjects++;

  return object;
}

/***************************
 push a int to a VM by calling push()
***************************/
void pushInt(VM* vm, int intValue)
{
  Object* object = newObject(vm, OBJ_INT);
  object->value = intValue;

  push(vm, object);
}

/***************************
 push a pair to a VM by calling push()
***************************/
Object* pushPair(VM* vm)
{
  Object* object = newObject(vm, OBJ_PAIR);
  object->tail = pop(vm);
  object->head = pop(vm);

  push(vm, object);
  return object;
}

/***************************
 __str__ of object
***************************/
void objectPrint(Object* object)
{
  switch (object->type)
  {
    case OBJ_INT:
      printf("%d", object->value);
      break;

    case OBJ_PAIR:
      printf("(");
      objectPrint(object->head);
      printf(", ");
      objectPrint(object->tail);
      printf(")");
      break;
  }
}

/***************************
 free the whole Virtual Machine
***************************/
void freeVM(VM *vm)
{
  vm->stackSize = 0;
  printf("\n");
  printf("Force free elements in VM:\n");
  gc(vm);
  free(vm);
}

void test1()
{
  printf("Test 1: Objects on stack are preserved.\n");
  VM* vm = newVM();
  pushInt(vm, 1);
  pushInt(vm, 2);

  gc(vm);
  assert(vm->numObjects == 2, "Should have preserved objects.");
  freeVM(vm);
}

void test2()
{
  printf("Test 2: Unreached objects are collected.\n");
  VM* vm = newVM();
  pushInt(vm, 1);
  pushInt(vm, 2);
  pop(vm);
  pop(vm);

  gc(vm);
  assert(vm->numObjects == 0, "Should have collected objects.");
  freeVM(vm);
}

void test3()
{
  printf("Test 3: Reach nested objects.\n");
  VM* vm = newVM();
  pushInt(vm, 1);
  pushInt(vm, 2);
  pushPair(vm);
  pushInt(vm, 3);
  pushInt(vm, 4);
  pushPair(vm);
  pushPair(vm);

  gc(vm);
  assert(vm->numObjects == 7, "Should have reached objects.");
  freeVM(vm);
}

void test4()
{
  printf("Test 4: Handle cycles.\n");
  VM* vm = newVM();
  pushInt(vm, 1);
  pushInt(vm, 2);
  Object* a = pushPair(vm);
  pushInt(vm, 3);
  pushInt(vm, 4);
  Object* b = pushPair(vm);

  a->tail = b;
  b->tail = a;

  gc(vm);
  assert(vm->numObjects == 4, "Should have collected objects.");
  freeVM(vm);
}

void perfTest()
{
  printf("Performance Test.\n");
  VM* vm = newVM();

  for (int i = 0; i < 1000; i++)
  {
    for (int j = 0; j < 20; j++)
    {
      pushInt(vm, i);
    }

    for (int k = 0; k < 20; k++)
    {
      pop(vm);
    }
  }
  freeVM(vm);
}

int main(int argc, const char * argv[])
{
  test1();
  test2();
  test3();
  test4();
  perfTest();
  
  getchar();
  return 0;
}
