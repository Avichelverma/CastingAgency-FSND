PGDMP                         x           castingagency    12.3    12.3     !           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            "           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            #           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            $           1262    41050    castingagency    DATABASE     �   CREATE DATABASE castingagency WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'English_India.1252' LC_CTYPE = 'English_India.1252';
    DROP DATABASE castingagency;
                postgres    false            �            1259    41066    actor    TABLE     �   CREATE TABLE public.actor (
    id integer NOT NULL,
    name character varying NOT NULL,
    age integer,
    gender character varying
);
    DROP TABLE public.actor;
       public         heap    postgres    false            �            1259    41064    actor_id_seq    SEQUENCE     �   CREATE SEQUENCE public.actor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.actor_id_seq;
       public          postgres    false    205            %           0    0    actor_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.actor_id_seq OWNED BY public.actor.id;
          public          postgres    false    204            �            1259    41090    alembic_version    TABLE     X   CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);
 #   DROP TABLE public.alembic_version;
       public         heap    postgres    false            �            1259    41055    movie    TABLE     �   CREATE TABLE public.movie (
    id integer NOT NULL,
    title character varying NOT NULL,
    release_date timestamp without time zone
);
    DROP TABLE public.movie;
       public         heap    postgres    false            �            1259    41051    movie_id_seq    SEQUENCE     �   CREATE SEQUENCE public.movie_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.movie_id_seq;
       public          postgres    false    203            &           0    0    movie_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.movie_id_seq OWNED BY public.movie.id;
          public          postgres    false    202            �            1259    41075 
   movie_list    TABLE     a   CREATE TABLE public.movie_list (
    movie_id integer NOT NULL,
    actor_id integer NOT NULL
);
    DROP TABLE public.movie_list;
       public         heap    postgres    false            �
           2604    41069    actor id    DEFAULT     d   ALTER TABLE ONLY public.actor ALTER COLUMN id SET DEFAULT nextval('public.actor_id_seq'::regclass);
 7   ALTER TABLE public.actor ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    204    205    205            �
           2604    41058    movie id    DEFAULT     d   ALTER TABLE ONLY public.movie ALTER COLUMN id SET DEFAULT nextval('public.movie_id_seq'::regclass);
 7   ALTER TABLE public.movie ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    203    202    203                      0    41066    actor 
   TABLE DATA           6   COPY public.actor (id, name, age, gender) FROM stdin;
    public          postgres    false    205   �                 0    41090    alembic_version 
   TABLE DATA           6   COPY public.alembic_version (version_num) FROM stdin;
    public          postgres    false    207   a                 0    41055    movie 
   TABLE DATA           8   COPY public.movie (id, title, release_date) FROM stdin;
    public          postgres    false    203   ~                 0    41075 
   movie_list 
   TABLE DATA           8   COPY public.movie_list (movie_id, actor_id) FROM stdin;
    public          postgres    false    206   �       '           0    0    actor_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.actor_id_seq', 17, true);
          public          postgres    false    204            (           0    0    movie_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.movie_id_seq', 17, true);
          public          postgres    false    202            �
           2606    41074    actor actor_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.actor
    ADD CONSTRAINT actor_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.actor DROP CONSTRAINT actor_pkey;
       public            postgres    false    205            �
           2606    41094 #   alembic_version alembic_version_pkc 
   CONSTRAINT     j   ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);
 M   ALTER TABLE ONLY public.alembic_version DROP CONSTRAINT alembic_version_pkc;
       public            postgres    false    207            �
           2606    41079    movie_list movie_list_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.movie_list
    ADD CONSTRAINT movie_list_pkey PRIMARY KEY (movie_id, actor_id);
 D   ALTER TABLE ONLY public.movie_list DROP CONSTRAINT movie_list_pkey;
       public            postgres    false    206    206            �
           2606    41063    movie movie_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.movie
    ADD CONSTRAINT movie_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.movie DROP CONSTRAINT movie_pkey;
       public            postgres    false    203            �
           2606    41085 #   movie_list movie_list_actor_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.movie_list
    ADD CONSTRAINT movie_list_actor_id_fkey FOREIGN KEY (actor_id) REFERENCES public.actor(id);
 M   ALTER TABLE ONLY public.movie_list DROP CONSTRAINT movie_list_actor_id_fkey;
       public          postgres    false    205    2708    206            �
           2606    41080 #   movie_list movie_list_movie_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.movie_list
    ADD CONSTRAINT movie_list_movie_id_fkey FOREIGN KEY (movie_id) REFERENCES public.movie(id);
 M   ALTER TABLE ONLY public.movie_list DROP CONSTRAINT movie_list_movie_id_fkey;
       public          postgres    false    206    2706    203               e   x�5�;
�0 �9=EO �/΢�����$�@S���.]�3���QO$��c��a$AG��92靝c��KW�L��EA/��'AѤ�`A�=���M|dJ��"�            x������ � �         M   x�3�.-H-�M��4202�50�5�P00�20�20�2��M,*K�I��K�pV�����Krd���Ő����� T�            x������ � �     