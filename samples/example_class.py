class MyClass:
  """A simple example class"""
  i = 12345
  def f(self):
    return 'hello world'
  def i(self):
    return self.i

a = MyClass()
print a.i()
print 'hi'
