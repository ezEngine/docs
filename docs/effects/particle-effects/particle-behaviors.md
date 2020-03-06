# Particle Behaviors

This page lists and describes all *particle behaviors*.

## Color Gradient Behavior

This behavior changes a particle's color during the update step. A [color gradient](../../animation/color-gradients.md) is used as the color source, and a mode specifies how to look up the color from the gradient.

**Gradient:** The [color gradient](../../animation/color-gradients.md) to use as the source.

**TintColor:** An additional color to be multiplied into the gradient, for tweaking the final result.

**ColorFrom:** This mode specifies how the color is looked up from the gradient:

* `Age` - In this mode the particle's color depends on its age and remaining lifetime. That means it starts out with the leftmost color from the gradient and transitions towards the rightmost color. Optimally, the color gradient should include alpha values, such that the particles can fade out towards the end.
* `Speed` - In this mode the particle's color is determined from its current speed. Slow particles are assigned colors from the left side of the gradient, fast particles that from the right side. This mode only makes sense when either every particle gets a random speed assigned, or when its speed is able to change over time, due to friction, gravity or other factors.

**MaxSpeed:** When using *ColorFrom = Speed*, this value specifies the maximum expected speed of any particle. That speed is then mapped to the rightmost side of the color gradient.

## Fade Out Behavior

This behavior changes a particle's alpha value to gradually fade out over its lifetime.

**StartAlpha:** The alpha value to begin with when the particle has just spawned.

**Exponent:** How quickly to fade the alpha value from `StartAlpha` towards `0` over the particle's lifespan. An exponent of `1` results in a linear fade. An exponent of `2` will make it fade out much earlier, a value of `0.5` will make it fade out very slowly at first and then quite abruptly at the end.

## Flies Behavior

This behavior moves particles around the emitter center in erratic patterns, similar to a swarm of flies circling something.

**FlySpeed:** The speed with which the particles move.

**PathLength:** The distance that the particles move into some direction before making another turn. The shorter this is, the more often the particles can change direction and thus the smoother the motion becomes. They will also clump up more and stay within the *MaxEmitterDistance*, if the particles can correct their course more often. With a long *PathLength* they may spread out more.

**MaxEmitterDistance:** The maximum distance that the particles will fly away from the effect's center before turning back. If they travel further, they will always steer back towards the emitter. How quickly that is possible though, depends on *PathLength* and *MaxSteeringAngle*.

**MaxSteeringAngle:** Every time a particle has traveled a distance of *PathLength*, it will make a random turn. This value specifies how large that turn may be. A small value results in very slow and wide turns, whereas a large value results in quick and erratic behavior.


<video width="500" height="500" controls>
  <source src="media/flies.webm" type="video/webm">
</video>

## Gravity Behavior

**GravityFactor:**

## Pull Along Behavior

**Strength:**

## Raycast Behavior

**Reaction:**

**BounceFactor:**

**CollisionLayer:**

**OnCollideEvent:**

## Size Curve Behavior

**SizeCurve:**

**BaseSize:**

**CurveScale:**

## Velocity Behavior

**RiseSpeed:**

**Friction:**

**WindInfluence:**

## See Also

* [Back to Index](../../index.md)
* [Particle Effects (TODO)](particle-effects-overview.md)
