import { useState, useEffect } from "react";
import axios from "axios";
import Carousl from "../Carousel/Carousl";

export default function Cards() {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios
      .get("/api/home/movies")
      .then((response) => {
        setPosts(Array.isArray(response.data.data) ? response.data.data : []);
      })
      .catch((error) => {
        console.error(error);
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  return (
    <section>
      {loading ? (
        <p className="text-gray-500">Loading movies...</p>
      ) : (
        <Carousl movies={posts} />
      )}
    </section>
  );
}
