"use client";
import { useState } from "react";
import {LoaderCircle} from "lucide-react"
import useStore from "@/utils/store";

export default function Home() {
  const [content, setContent] = useState<string>("");
  const [role, setRole] = useState<string>("");
  const [score, setScore] = useState<string>("0");
  const [loader,setLoader] = useState<boolean>(false);
  const {url} = useStore();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoader(true);
    try{
      const resp = await fetch(`${url}/resume/predict`,{
        method:"POST",
        headers:{
          "content-type" : "application/json"
        },
        body:JSON.stringify({resume:content})
      });

      const parsedResp = await resp.json();
      if(!resp.ok ) throw new Error("Server is down.")
      setRole(parsedResp.predicted_role);
      setScore(parsedResp.match_score);
    }catch(err){ 
      console.error(err);
      return alert("Unable to proceed.")
    }finally{
      setLoader(false);
      setContent("");
    }
  };

  return (
    <div className="min-h-screen w-full bg-linear-to-br from-gray-100 to-gray-300 flex items-center justify-center px-4">
      
      <div className="w-full max-w-4xl bg-white shadow-2xl rounded-3xl p-8 space-y-8">
        
        <div className="text-center space-y-2">
          <h1 className="text-4xl font-bold text-gray-800">
            Job Role Predictor
          </h1>
          <p className="text-gray-500">
            Paste your resume and let AI suggest your best-fit role
          </p>
        </div>

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label
              htmlFor="resume-content"
              className="block text-lg font-medium text-gray-700"
            >
              Resume Content
            </label>
            <p className="text-sm text-orange-500">
              Include your skills for better predictions*
            </p>
          </div>

          <textarea
            id="resume-content"
            placeholder="Paste your resume here..."
            value={content}
            onChange={(e) => setContent(e.target.value)}
            className="w-full text-black h-48 p-4 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-black resize-none transition"
          />

          <button
            type="submit"
            className="w-full bg-black text-white py-3 rounded-xl grid place-items-center font-semibold hover:bg-gray-800 active:scale-[0.98] transition"
          >
            {
              loader ? <LoaderCircle className="animate-spin"/> : "Predict Role"
            }
            
          </button>
        </form>

        <div className="bg-gray-50 rounded-2xl p-6 space-y-3 border">
          <h2 className="text-xl font-semibold text-gray-800">Result</h2>

          <div className="flex justify-between text-lg">
            <span className="text-gray-600">Predicted Role:</span>
            <span className="font-semibold text-black">{role || "-"}</span>
          </div>

          <div className="flex justify-between text-lg">
            <span className="text-gray-600">Score:</span>
            <span className="font-semibold text-black">{score}</span>
          </div>
        </div>
      </div>
    </div>
  );
}