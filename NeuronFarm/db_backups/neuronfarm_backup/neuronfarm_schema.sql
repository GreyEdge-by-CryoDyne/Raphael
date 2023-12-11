GRANT SELECT,INSERT,UPDATE ON TABLE public.accesslogs TO the_grey;


--
-- Name: TABLE metadata; Type: ACL; Schema: public; Owner: grey
--

GRANT SELECT,INSERT,UPDATE ON TABLE public.metadata TO the_grey;


--
-- Name: TABLE parseddata; Type: ACL; Schema: public; Owner: grey
--

GRANT SELECT,INSERT,UPDATE ON TABLE public.parseddata TO the_grey;


--
-- Name: TABLE systemlogs; Type: ACL; Schema: public; Owner: grey
--

GRANT SELECT,INSERT,UPDATE ON TABLE public.systemlogs TO the_grey;


--
-- Name: TABLE users; Type: ACL; Schema: public; Owner: grey
--

GRANT SELECT,INSERT,UPDATE ON TABLE public.users TO the_grey;


--
-- Name: DEFAULT PRIVILEGES FOR TABLES; Type: DEFAULT ACL; Schema: public; Owner: grey
--

ALTER DEFAULT PRIVILEGES FOR ROLE grey IN SCHEMA public GRANT SELECT,INSERT,DELETE,UPDATE ON TABLES  TO grey;


--
-- Name: DEFAULT PRIVILEGES FOR TABLES; Type: DEFAULT ACL; Schema: public; Owner: postgres
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT SELECT,INSERT,DELETE,UPDATE ON TABLES  TO grey;


--
-- PostgreSQL database dump complete
--


