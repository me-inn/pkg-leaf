// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// One entry point, so a consumer writes `from '@me-inn/leaf'` and never a path
// into this repository's layout. The layout is ours to change; the names are
// the contract.
export type { Organization, TaxIdentifier, ContactPoint } from './organization';
export type { Person } from './person';
export type { Membership, Status as MembershipStatus } from './membership';
export type { Participation, Context as ParticipationContext, Status as ParticipationStatus } from './participation';