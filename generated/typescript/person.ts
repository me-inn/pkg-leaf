// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * A person. Holds no authentication secret: password hashes, reset tokens and auth
 * providers belong to the system that authenticates.
 */
export interface Person {
    /**
     * Ways to reach them.
     */
    contacts?: ContactPoint[];
    /**
     * ISO 3166-1 alpha-2, where they are registered.
     */
    country?:   string;
    createdAt?: Date;
    /**
     * The name they are known by.
     */
    displayName: string;
    /**
     * Their public address, without the @.
     */
    handle?: string;
    locale?: Locale;
    /**
     * The id this person has in each system that holds a record of them.
     */
    localIds?: { [key: string]: string };
    /**
     * Their tax or registry identifiers, one per scheme.
     */
    taxIds?: TaxIdentifier[];
    /**
     * ed25519 public key, hex. Identifies the person. Absent until they hold one.
     */
    wallet?: string;
}

/**
 * One way to reach an actor.
 */
export interface ContactPoint {
    /**
     * The language to write to this point in.
     */
    locale?: Locale;
    /**
     * Which channel the value is for.
     */
    type: Type;
    /**
     * An address, or a number in E.164 digits including the country code.
     */
    value:       string;
    verified?:   boolean;
    verifiedAt?: Date;
}

/**
 * The language to write to this point in.
 */
export type Locale = "pt" | "en" | "es";

/**
 * Which channel the value is for.
 */
export type Type = "email" | "whatsapp" | "mobile" | "phone";

/**
 * A tax or registry identifier.
 */
export interface TaxIdentifier {
    /**
     * ISO 3166-1 alpha-2, when the scheme does not imply one.
     */
    country?: string;
    /**
     * URL of the supporting document.
     */
    documentUrl?: string;
    /**
     * The scheme, such as CNPJ, CPF, NIF, VAT or EIN. Free text, always stated, never inferred
     * from the length of the value.
     */
    type:  string;
    value: string;
}