# Particle Effects

<!-- PAGE IS TODO -->

Particle effects are used to create the visual part of things like explosions, smoke, fire, water splashes and much more. They are randomized to have slight variations every time. To create a full effect, like an explosion, with [sound (TODO)](../../sound/sound-overview.md) and physical properties such as pushing nearby objects away or damaging objects and creatures, a particle effect is typically put into a [prefab (TODO)](../../prefabs/prefabs-overview.md), which contains additional components for sound and game play logic (e.g. through [scripts (TODO)](../../custom-code/typescript/typescript-overview.md)).

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

The **Effect** panel lists options for the overall effect, independent of the individual particle systems. Adjusting these options is typically only necessary once an effect is working well and you need to tweak its performance or allow users to adjust details through [exposed parameters (TODO)](../../scenes/exposed-parameters.md).

### Emitter, Initializers, Behaviors and Renderers

These panels show the various options for the *active particle system*. When you select a different particle system from the combo box in the *Systems* panel, these panels will show different options.

### Event Reactions

Particles may raise *events*. The most common one is when a particle dies, but different particle behaviors can raise other events as well. For example when a particle collides with the environment.

*Event reactions* allow to configure what happens for a specific event. This is mostly used to chain effects. For example a fireworks effect has particles that represent the rockets flying up, and when one 'dies', a big explosion is spawned at that position, using event reactions.

## Particle System Configuration

Every particle system has exactly one *emitter*, usually multiple *initializers* and *behaviors*, and typically one *renderer*. Most parameters are configured on those parts.

Additionally, every particle system has these properties:

**Visible:** This is an option for testing. If *Visible* is deactivated, the particle system is not simulated or rendered. Use this when you need to focus on editing other systems, or when a particle system is not yet good enough to be used. Invisible particle systems don't cost performance.

**Life:** This is a [value with variance](#variance-values). It specifies how long each particle will be simulated and rendered before it is removed from the system. A low variance means all particles live equally long, a high variance means some will have a short lifespan, others a much longer one.

**LifeScaleParam:** An optional [effect parameter](#effect-parameters) which can be used to scale the particle lifespan.

**OnDeathEvent:** An optional name for the [event](#events) when a particle dies. This can be used to spawn other effects.

### Emitter

The *emitter* is what defines how new particles in this system get spawned. It mostly specifies when and how many particles are spawned. Typically particles are either spawned in one big burst or continuously. However, for advanced use cases the emitter may only spawn particles as a reaction to some [event](#events) or when the particle effect node was moved a certain distance.

For details about all available emitter types, see [Particle Emitters (TODO)](particle-emitters.md).

### Initializers


For details about all available initializer types, see [Particle Initializers (TODO)](particle-initializers.md).

### Behaviors


For details about all available behavior types, see [Particle Behaviors (TODO)](particle-behaviors.md).

### Renderers


For details about all available renderer types, see [Particle Renderers (TODO)](particle-renderers.md).

## Effect Parameters

## Events

## Misc

### Variance Values

The particle editor presents many values as *values with variance*. They appear as a single value with a slider next to it:

![Variance Value](media/variance-value.png)

The input box represents the *base value* and the slider represents the *variance*. The variance is between `0` and `1`.

Generally, this type represents a random value, centered around the base value using a [normal distribution](https://en.wikipedia.org/wiki/Normal_distribution). The variance affects the range from which random values are drawn. The range is always between `BaseValue - Variance*BaseValue` and `BaseValue + Variance*BaseValue`. Consequently:

* If `Variance` is `0`, the range and thus the result for every 'random' value will be exactly `BaseValue`.
* If the variance is `1`, the random value will be anywhere between `0` and `2 * BaseValue`.
* For a variance of `0.5`, the random value will be between `BaseValue - 0.5*BaseValue` and `BaseValue + 0.5*BaseValue`

However, due to the *normal distribution* of the random numbers, values close to `BaseValue` will appear much more often than values far away from it. Such distributions are common in nature and therefore the result looks more natural.

For most such values you should use at least some variance (0.2 to 0.4) to make you effects look less repetitive and sterile. However, extremely large variance values (0.7 and up) can result in unexpected outliers.

## See Also

* [Back to Index](../../index.md)
* [How Particle Effects Work](how-particle-effects-work.md)
