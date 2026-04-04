"use client"

import React , { createContext ,useContext, useEffect} from 'react'
type ContextType = {
    url : string;
}

const Store = createContext<ContextType|undefined>(undefined);


function StoreProvider({children}:{children:React.ReactNode}) {
    const url = "https://job-role-predictor-latest.onrender.com";
    const wakeUpServer = async()=>{
        try{

            const resp = await fetch(`${url}`,{
                method:"GET",
                headers:{
                    "content-type":"application/json"
                }
            });
            
            const parsedResp = await resp.json();
            if(!resp.ok) return console.error("Server is unhealthy.");
            console.log(parsedResp.message);
        }catch(err){
            console.error(err);
            console.log("Server is not running");
        }
    }


    useEffect(()=>{
        wakeUpServer();
    },[])
  return (
    <Store.Provider value={{url}}>
        {children}
    </Store.Provider>
  )
}


const useStore = () => {
  const context = useContext(Store);
  if (!context) {
    throw new Error("useStore must be used within StoreProvider");
  }
  return context;
};

export { StoreProvider };
export default useStore;