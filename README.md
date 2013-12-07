# TDD Katas

Hi! So you want to learn TDD or get better at it? Great. For all the following Katas follow these rules exactly.
 
 * Read the requirements carefully.
 * Stick to the rules of TDD strictly.
 * Do one step at a time. 
 * Don't look ahead.
 
You may want to use this Python `unittest` template.

```python

	import unittest

	# here goes your production code

	class SomeTest(unittest.TestCase):

		def test_fail(self):
			self.fail()

		def test_something(self):
			self.assertTrue(True)


	if __name__ == '__main__':
		unittest.run()
```

You can now run your test like this:

```bash
    $: python thatfile.py
```

Maybe you want to install `watchdog`.
```bash
    $: pip install watchdog
```
Now you can run your tests each time you save `thatfile.py`.
```bash
    $: watchmedo shell-command --patterns="*.py" --command="clear; python thatfile.py" .
```
 

## Webshop total order amount
Given we run a webshop and customers can compile an order consisting of several items, I want to calculate the total order amount.
 
 1. VAT needs to be applied
 1. postage is 5$ 
 1. orders above 50$ get free shipping 


## Vowel counter

## FizzBuzz
