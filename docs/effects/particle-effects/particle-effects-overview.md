# Particle Effects

<!-- PAGE IS TODO -->

Particle effects are used to create the visual part of things like explosions, smoke, fire, water splashes and much more. They are randomized to have slight variations every time. To create a full effect, like an explosion, with sound and physical properties such as pushing nearby objects away or damaging objects and creatures, a particle effect is typically put into a [prefab (TODO)](../../prefabs/prefabs-overview.md), which contains additional components for [sound (TODO)](../../sound/fmod.md) and game play logic (e.g. through [scripts (TODO)](../../custom-code/typescript/typescript-overview.md)).

To create a new particle effect, use *Editor > Create Document* and select *Particle Effect* as the file type. Or alternatively, right-click on any asset in the [asset browser](../../assets/asset-browser.md) and select *New > Particle Effect*.

## Particle Editor UI

This is an overview screenshot of the particle editor:

![The particle editor](../media/particle-overview.png)

The 3D viewport plays the effect in a loop. Using the toolbar buttons you can pause, reset, slow down or speed up the playback. On the right hand side there are multiple tabs which hold the various settings of the effect. If you are not too familiar with particle effects yet, please read [how particle effects work](how-particle-effects-work.md).

On the right hand side you see multiple tabbed panels:

### Systems

The **Systems** panel is very central. Here you add new particle systems to the effect. However, this is also where you **select which particle system to edit**. The combo box specifies which particle system is currently active. All panels below (*Emitter*, *Initializers*, *Behaviors* and *Renderers*) show only the settings of the *active particle system*.

When you add a new particle system with the green '+' button, you get a new system that uses a default configuration.

### Effect

The **Effect** panel lists options for the overall effect, independent of the individual particle systems. Adjusting these options is typically only necessary once an effect is working well and you need to tweak its performance or allow users to adjust details through exposed parameters.

### Emitter, Initializers, Behaviors and Renderers

These panels show the various options for the *active particle system*. When you select a different particle system from the combo box in the *Systems* panel, these panels will show different options.

### Event Reactions

Particles may raise *events*. The most common one is when a particle dies, but different particle behaviors can raise other events as well. For example when a particle collides with the environment.

*Event reactions* allow to configure what happens for a specific event. This is mostly used to chain effects. For example a fireworks effect has particles that represent the rockets flying up, and when one 'dies', a big explosion is spawned at that position, using event reactions.




## See Also

* [Back to Index](../../index.md)
* [How Particle Effects Work](how-particle-effects-work.md)
