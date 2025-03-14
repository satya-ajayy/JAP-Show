function formatCompactNumber(num) {
  return new Intl.NumberFormat("en", { notation: "compact" }).format(num);
}

function genreforamtter(genre) {
  return genre.join(" / ");
}

export default function Card({ image_url, rating, votes, title, genre }) {
  return (
    <article className="card flex justify-between font-sans w-50 h-auto">
      <figure>
        <img className="w-50 h-75" src={image_url} alt="Movie Image" />
      </figure>
      <footer className="flex bg-black text-white ">
        <h2 className="p-1">⭐</h2>
        <h4 className="p-1 flex-1">{rating}/10</h4>
        <p className="p-1 flex-2">{formatCompactNumber(votes)}</p>
      </footer>
      <header className="bg-gray-100 text-wrap">
        <h1>{title}</h1>
        <p>{genreforamtter(genre)}</p>
      </header>
    </article>
  );
}
