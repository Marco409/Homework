class Stack:
  def __init__(self):
      self.stack = [None, None, None, None, None, None, None, None, None, None]
      self.top = -1
  def push(self, item):
      self.top += 1
      self.stack.append(item)
  def pop(self):
      if not self.is_empty():
          return self.stack.pop()
      else:
          raise IndexError("pop from empty stack")
  def peek(self):
      if not self.is_empty():
          return self.stack[-1]
      else:
          raise IndexError("peek from empty stack")
  def is_empty(self):
      return len(self.stack) == 0
  def size(self):
      return len(self.stack)

print(Stack.push())
