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
public:
    void push(int x) {
        element.push(x);
        if(minimum.empty() || x <= minimum.top()) {
            minimum.push(x);
        }
    }

    void pop() {
        if(minimum.empty()) {
            return;
        }

        if(element.top() == minimum.top()) {
            minimum.pop();
        }

        element.pop();
    }

    int top() {
        return element.top();
    }

    int getMin() {
        return minimum.top();
    }

private:
    stack<int> element;
    stack<int> minimum;
};


