# Development Log

## Date: September 25, 2026
**What I did:** Wrote an automated unit test using `pytest` to verify that the `Transaction` class correctly instantiates and formats its attributes.
**What confused me:** The test failed with `AttributeError: 'Transaction' object has no attribute 't_type'`. 
**How I figured it out:** I looked closely at the `pytest` failure summary, which actually suggested `Did you mean: 'type'?`. I realized that while the internal parameter was named `t_type` in the constructor, I had encapsulated it using a `@property` decorator named `type`. I updated the assertion to `assert t.type == "income"` and the test passed.