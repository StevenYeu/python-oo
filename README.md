# OO Desigin Pattersn

Python example of serveral design patterns

# Creational Patterns

## Factory Method

### Description 
Provide an interface for creating objects.

Allows subtypes or subclasses to create new objects

### When to use
- If types and dependacies are unknown before hand
    - Decouples object construction from object use
    - Easier to extend or add new objects
- Reuse of objects (i.e pool of objects)
    - If there no availble objects, create new one and add to pool
### Drawbacks
- Introduction of many subclasses or interfaces may introduce unwanted 
complexity
- 
### Implementation
- Create interface for objects
- Create interface for factory
- Create concrete objects/subclasses based on the object interface
- Create concrete factories that create concrete objects baseed on
    the factory interface

## Abstract Factory

### Description
Allows you create a group of related objects

### When to use
- When code nees to work with a group of realated objects
    - Ex: Groups of objects have same type of variants or theme

### Drawbacks
- Similar to Factory, depending on the number of variants and related objects
could introduce a lot of addtional interfaces and classes

### Implementation
- Create intefaces for each distanct object
- Create an interface for a factory that can create each disticnt object
- Create concrete Implementation for each product and it's variants
- Create concrete factories for each variant


## Builider 

### Description
Allows creations of complex objects step by step

### When to use
- Consider when object constructor has many parameteres 
(telescoping constructor)
- Create different version of the same product 
    - When construction of object has similar steps
    - Use construction code for variants

### Drawbacks 
- Would need to introduce new builder classes for each object with distinct 
construction

### Implementation
- Create an inteface for a builder of objects with similar construction steps
- Create concrete builders 
    - Each construction step should return a reference back to the builder
        - Can chain build steps together
    - Should have a `build`  step that returns constructed object

## Singleton

