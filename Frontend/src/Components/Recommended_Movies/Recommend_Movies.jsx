import Cards from "../Cards/Cards";

export default function Recommend_Movies() {
  return (
    <div className="h-120 ml-37 mr-37 mt-50">
      <div className="flex justify-between h-8">
        <h1 className="ml-1 font-bold">Recommended Movies</h1>
        <a href="" className="mr-15">
          See All
        </a>
      </div>
      <Cards />
    </div>
  );
}
