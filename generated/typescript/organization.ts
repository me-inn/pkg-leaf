// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * An organisation.
 */
export interface Organization {
    /**
     * Ways to reach it.
     */
    contacts?: ContactPoint[];
    /**
     * ISO 3166-1 alpha-2 country of registration.
     */
    country?:   string;
    createdAt?: Date;
    /**
     * The name it is known by.
     */
    displayName: string;
    isActive?:   boolean;
    /**
     * The name it is registered under.
     */
    legalName?: string;
    /**
     * The id this organisation has in each system that holds a record of it.
     */
    localIds?: { [key: string]: string };
    /**
     * URL-safe handle, lowercase.
     */
    slug?: string;
    /**
     * Its tax or registry identifiers, one per scheme.
     */
    taxIds?:    TaxIdentifier[];
    updatedAt?: Date;
    /**
     * ed25519 public key, hex. Identifies the organisation. Absent until it holds one.
     */
    wallet?:  string;
    website?: string;
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