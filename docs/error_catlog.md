1. SchemaMismatch
What it is

The structure of the data is different from what the pipeline expects
(for example, column names or data types do not match).

Why it happens

Column renamed (e.g., User_ID → ID)

Data type changed (e.g., numeric Price becomes "Contact for Price")

Extra or unexpected columns added

Impact

Pipeline may crash

Or produce incorrect results

Fix

Validate schema before model input

Convert data types properly

Define strict schema rules

Prevention

Enforce schema contracts

Fail early when schema changes

Add validation tests

2. MissingColumn
What it is

A required feature or column is completely missing.

Why it happens

Dropped during preprocessing

API or database did not send it

Developer forgot to extract it

Fix

Restore or backfill missing features

Update extraction logic

Prevention

Automatic checks for required features

Schema validation before inference

3. DataQuality
What it is

The pipeline runs, but the data is invalid or unreliable.

Common issues

Missing values

Impossible values (e.g., Age = −500)

Duplicate rows

Data drift over time

Garbage In → Garbage Out

Fix

Clean missing values

Handle outliers

Remove duplicates

Monitor drift

Prevention

Add validation rules

Track data distributions

4. ShapeMismatch
What it is

The size (shape) of the data does not match what the model expects.

Why it happens

Wrong batch size

Incorrect reshape

Deep-learning layer mismatch

Fix

Check and verify tensor shapes

Standardize feature pipeline

Prevention

Shape checks in preprocessing

Unit tests for input format

5. ResourceLimit
What it is

The system runs out of compute or memory.

Common examples

CUDA Out-of-Memory (GPU)

RAM exhausted

Disk quota exceeded

Process killed by OS

Impact

Training or inference stops mid-run

Fix

Reduce batch size

Use a smaller model

Enable mixed precision

Increase resources

Prevention

Resource monitoring

Memory-efficient pipelines

6. TrainingInstability
What it is

Training runs, but becomes unstable.

Common signals

Loss becomes NaN

Exploding gradients

Diverging metrics

Fix

Reduce learning rate

Clip gradients

Normalize inputs

Check labels

Prevention

Training sanity checks

Early alerts on drift

7. ConvergenceFailure
What it is

The model never converges to a useful state.

Why it happens

Bad hyperparameters

Poor initialization

Wrong optimizer

Incorrect feature scaling

Fix

Tune learning rate or batch size

Improve feature normalization

Try alternate optimizers

Prevention

Baseline models

Training experiment discipline

8. Unknown
What it is

The system cannot confidently classify the error.

Why it happens

New or unusual failure

Incomplete logs

Weak signal

Behavior

The system prefers to stay honest
instead of guessing incorrectly.

Fix

Review logs manually

Improve rules later

Summary
Error Type	Meaning
SchemaMismatch	Data structure changed
MissingColumn	Required field missing
DataQuality	Data is messy or invalid
ShapeMismatch	Data size doesn’t match
ResourceLimit	System ran out of compute or memory
TrainingInstability	Training became unstable
ConvergenceFailure	Model failed to converge
Unknown	Not enough signal to classify
Philosophy

Rules decide.
Retrieval only explains.

This keeps the system:

Predictable

Explainable

Reliable