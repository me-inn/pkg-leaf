# leaf

**The shape of the data, not the data.** Each system keeps its own database;
only the shape is shared.

## Why it exists

When several systems exchange data, whoever consumes it ends up redeclaring
the structure on their own side — and every redeclaration can drift on its
own. N systems talking pairwise produce N×(N−1)/2 translations of the same
thing.

Here the shape is declared once. The data stays where it is.

## How it works

One file, written by hand, once:

```
schemas/common.v1.json          TaxIdentifier, ContactPoint, LocalIds
schemas/organization.v1.json    an organisation
schemas/person.v1.json          a person
schemas/membership.v1.json      person ↔ organisation
schemas/participation.v1.json   organisation ↔ context
```

And each language's types are generated from it:

```
generated/dart/
generated/rust/
generated/typescript/
generated/python/
```

```bash
./generate.sh
```

**Nobody writes those classes.** They are generated, checked in so a consumer
can read them without running anything, and CI regenerates and compares:
**editing one by hand breaks the build.** Not an agreement between people — an
impossibility.

## Edges, not columns

An organisation's role — sponsor of an event, seller in a split, publisher of
a title — is not an attribute of the organisation. They are different
relationships, and as a column each new context would add another set of
values to a field that was never an attribute of the thing it sat on. That is
why `membership` and `participation` exist as edges.

## The key

An actor **is** its wallet key (ed25519). It is the only identifier that means
the same thing in every system holding a record about it. Until there is a
key, `localIds` says what each system calls it.

## Rules are not generated

A generator produces the type, never the invariant. Refusing an empty name in
a constructor does not come out of a schema.

So the pattern is **generated type, rule written by hand beside it** — never
inside. The generated file is untouchable.

## Secrets do not travel

`person` carries no password hash, no reset token, no auth provider.
Authentication secrets belong to whoever authenticates: a shared shape is read
by many systems, and a secret inside it would be a secret in all of them.

## Versioning

A new schema never edits an old one: `organization.v2.json` is born beside
`organization.v1.json`. Old data stays readable, and nothing in production
breaks because somebody added a field.

## Using it

```bash
npm install github:me-inn/pkg-leaf
```

```ts
import type { Organization, Person } from '@me-inn/leaf';
```

## Branches

`main` is the project. `docs` is where documents live.

## Licence

MIT. See `LICENSE`.
