CREATE TABLE public.cpi_series(
    ref_date TIMESTAMP NOT NULL UNIQUE,
    index_value DECIMAL NOT NULL
);