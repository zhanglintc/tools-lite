// Min Stack
// for leetcode problems
// 2014.12.12 by zhanglin

// Problem:
// Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

// push(x) -- Push element x onto stack.
// pop() -- Removes the element on top of the stack.
// top() -- Get the top element.
// getMin() -- Retrieve the minimum element in the stack.

class MinStack {
    private Stack<Integer> element = new Stack<Integer>();
    private Stack<Integer> minimum = new Stack<Integer>();

    public void push(int x) {
        element.push(x);

        if(minimum.isEmpty() || x <= minimum.peek()) {
            minimum.push(x);
        }
    }

    public void pop() {
        if(element.isEmpty()) {
            return;
        }

        if(element.peek().equals(minimum.peek())) {
            minimum.pop();
        }

        element.pop();
    }

    public int top() {
        return element.peek();
    }

    public int getMin() {
        return minimum.peek();
    }
}


